#include "lists.h"

/**
 * list_size - Returns the size of a singly-linked list.
 * @head: The head of the list.
 *
 * Return: The size of the list.
 */
size_t list_size(listint_t *head)
{
	listint_t *current;
	size_t len = 0;

	for (current = head; current; len++, current = current->next)
		;

	return (len);
}

/**
 * rev_listint - Reverses  a singly-linked list.
 * @head: The head of the list.
 */
void rev_listint(listint_t **head)
{
	listint_t *current, *next, *previous;

	current = *head;
	next = previous = NULL;
	while (current)
	{
		previous = current->next;
		current->next = next;
		next = current;
		current = previous;
	}
	*head = next;
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
	size_t len, i, half;

	if (!head)
		return (1);

	len = list_size(*head), half = len / 2;

	rev_head = NULL;
	for (i = 0, current = *head; i < half - 1; i++, current = current->next)
		;

	if (len % 2 != 0)
		current = current->next;
	rev_head = current;
	rev_listint(&rev_head);

	for (rev_curr = rev_head, current = *head; current;
	     current = current->next, rev_curr = rev_curr->next)
		if (current->n != rev_curr->n)
		{
			rev_listint(&rev_head);
			return (0);
		}

	rev_listint(&rev_head);
	return (1);
}
