#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - finds a loop in a linked list
 * @list: list to take in
 * Return: 1 if loop 0 if no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = list;
	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
			return (1);
	}
	return (0);
}
