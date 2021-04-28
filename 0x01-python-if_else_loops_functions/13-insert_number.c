#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node, *new_node;

	/* Iterable node through list. */
	current_node = *head;

	/* Create new node. */
	new_node = malloc(sizeof(*new_node));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	/* Case 1: if new node's number is less than list's head. */
	if (current_node->n > number)
	{
		new_node->next = current_node;
		return (new_node);
	}

	/* Case 2: if new node's number is less than the next node's one. */
	while (current_node != NULL)
	{
		if (current_node->next->n > number)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return (new_node);
		}
		current_node = current_node->next;
	}

	/* Case 3: if the new node's number is the greatest of the list. */
	current_node->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
