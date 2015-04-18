#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "msgstructs.h"

double ACCESS;

int sparent[2], rparent[2];

int cap[1] = { CAPVAL };

int recvQuery(query_t *query) {
	char capbuf[100];
	read(rparent[0], query, sizeof(query_t));
	read(rparent[0], capbuf, 100);

	return 0;
}

int sendResponse(response_t *response) {
	write(sparent[1], response, sizeof(response_t));
	write(sparent[1], cap, sizeof(cap));

	return 0;
}

int parseData(query_t *query, char *data) {
	char *prebuf;
	prebuf = strtok(query->data, ";"); // Read the "FROM <id>;" part

	data = strtok(NULL, "");

	return 0;
}

int checkCredentials(query_t *query) {
	return query->credentials > ACCESS;
}

int needPermissions(response_t *response) {
	response->status = FAILURE;
	snprintf(response->data, 0x100, "%s", "You need the requisite authentication to perform this action");

	return 0;
}

int handleRead(query_t *query, response_t *response) {
	if (!checkCredentials(query))
		return needPermissions(response);

	char fname[0x100];
	parseData(query, fname);

	if (access(fname, R_OK) == -1) {
		response->status = FAILURE;
		snprintf(response->data, 0x100, "%s", "Unable to read file");

		return 0;
	}
	
	FILE *file = fopen(fname, "r");
	int num = fread(response->data, 1, 0xff, file);
	response->data[num] = '\0';
	fclose(file);

	response->status = SUCCESS;

	return 0;
}

int handleExec(query_t *query, response_t *response) {
	if (!checkCredentials(query))
		return needPermissions(response);

	char command[0x100];
	parseData(query, command);

	int status = system(command);

	snprintf(response->data, 0x100, "Exit code: %d", status);
	response->status = SUCCESS;

	return 0;
}

int handleLogin(query_t *query, response_t *response) {
	char fname[0x100];

	sprintf(fname, "password.%ld.txt", query->userid);

	if (access(fname, R_OK) == -1) {
		response->status = FAILURE;
		snprintf(response->data, 0x100, "%s", "Invalid username or password");

		return 0;
	}

	char input[0x100];
	parseData(query, input);
	char password[0x100];
	
	FILE *file = fopen(fname, "r");
	int num = fread(password, 1, 0x100, file);
	fclose(file);
	
	if (!strncmp(password, input, num)) {
		double credentials = 0;
		switch(query->userid) {
			case 0:
				credentials = 1.0/0.0;
			case 1337:
				credentials = 50000;
			default:
				credentials = 5;
		}
		snprintf(response->data, 0x100, "%g is your new access level", credentials);
		response->status = SUCCESS;
	} else {
		response->status = FAILURE;
		snprintf(response->data, 0x100, "%s", "Invalid username or password");
	}

	return 0;
}

int handleStatus(query_t *query, response_t *response) {
	snprintf(query->data, 0x100, "FROM STATUS;status.txt");
	query->credentials = 1.0/0.0;

	return handleRead(query, response);
}

int handle(query_t *query, response_t *response) {
	switch (query->action) {
		case READ_ACTION:
			return handleRead(query, response);
		case EXEC_ACTION:
			return handleExec(query, response);
		case LOGIN_ACTION:
			return handleLogin(query, response);
		case STATUS_ACTION:
			return handleStatus(query, response);
		case SMILEY_ACTION:
			response->status = SUCCESS;
			snprintf(response->data, 0x100, "%s", "You are a star! :)");
			return 0;
		default:
			response->status = FAILURE;
			snprintf(response->data, 0x100, "%s", "Command not implemented");
			return 0;
	}
}

int run() {
	query_t query;
	response_t response;

	while (1) {
		recvQuery(&query);
		handle(&query, &response);
		sendResponse(&response);
	}

	return 0;
}

int setupAccess() {
	char buf[0x100];
	FILE *afile = fopen("access.txt", "r");
	int num = fread(buf, 1, 0xff, afile);
	buf[num] = '\0';
	ACCESS = strtod(buf, NULL);
	fclose(afile);

	return 0;
}

int setupPipes() {
	fread(rparent, sizeof(int), 2, stdin);
	fread(sparent, sizeof(int), 2, stdin);

	return 0;
}

int main(int argc, char **argv) {
	setupAccess();
	setupPipes();

	return run();
}

