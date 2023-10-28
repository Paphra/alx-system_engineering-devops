#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop to keep parent process alive
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - creates 5 process (zombies)
 * Return: 0 - for success, else 1
 */
int main(void)
{
	int i;
	pid_t zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie_pid);
	}
	infinite_while();

	return (0);
}
