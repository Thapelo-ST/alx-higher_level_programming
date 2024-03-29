#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - ...
 * @list: ...
 * Return: ...
 */

int check_cycle(listint_t *list)
{
	/*declare variale*/
	listint_t *old = list, *new = list;

	while (new && new->next)
	{
		/*assign variables*/
		old = old->next;
		new = new->next->next;
		/* if ther is a cycle*/
		if (old == new)
			return (1);
	}
	/*if there is no cycle*/
	return (0);
}
