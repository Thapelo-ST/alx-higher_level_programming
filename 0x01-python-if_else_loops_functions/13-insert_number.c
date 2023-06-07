#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - ...
 * @head: ...
 * @number: ...
 * Return: ...
 */
listint_t *insert_node(listint_t **head, int number)
{
	/*declare variable*/
	listint_t *node_n = malloc(sizeof(listint_t));
	listint_t *new;

	/*check validity*/
	if (node_n == NULL)
		return (NULL);
	/*assign number to value*/
	node_n->n = number;
	if (*head == NULL || number < (*head)->n)
	{
		node_n->next = *head;
		*head = node_n;
	}
	else
	{
		new = *head;
		while (new->next != NULL && number > new->next->n)
		{
			new = new->next;
		}
		node_n->next = new->next;
		new->next = node_n;
	}
	return (node_n);
}
