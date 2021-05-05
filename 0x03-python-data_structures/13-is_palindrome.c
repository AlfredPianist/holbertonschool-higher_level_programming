#include "lists.h"

/**
 * add_nodeint - Adds a node at the beginning of the list.
 * @head: The head of the list.
 * @n: The content of the node.
 *
 * Return: The new node of the list.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(*new_node));
	if (!new_node)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * is_palindrome - Verifies if a list is palindromic.
 * @head: The head of the list.
 *
 * Return: 0 if not palindromic, 1 if palindromic.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *rev_head, *rev_curr;

	if (!head)
		return (1);

	rev_head = NULL;

	for (current = *head; current; current = current->next)
		add_nodeint(&rev_head, current->n);

	for (current = *head, rev_curr = rev_head; current;
	     current = current->next, rev_curr = rev_curr->next)
		if (current->n != rev_curr->n)
		{
			free_listint(rev_head);
			rev_head = NULL;
			return (0);
		}

	free_listint(rev_head);
	return (1);
}
