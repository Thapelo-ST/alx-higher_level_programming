#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *n_l = NULL, *new_node = *head, *old = NULL, *new = NULL;

    if (*head == NULL)
        return (1);
    /* assign new list called new node*/
    while (new_node)
    {
        new = new_node->next;
        new_node->next = old;
        old = new_node;
        new_node = new;
    }
    n_l = old;
    /* find palindrome */
    new_node = *head;
    while (new_node != NULL && n_l != NULL)
    {
        if (new_node->n != n_l->n)
            return (0);
        new_node = new_node->next;
        n_l = n_l->next;
    }
    return (1);
}