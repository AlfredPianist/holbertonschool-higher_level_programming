#include "lists.h"

/**
 * check_cycle - Implementation of Floyd's cycle detection algorithm.
 * @list: The list's head.
 *
 * Description: This function detects if a linked list is a cycle or not.
 *              For this, we will need two nodes, a fast and a slow one.
 *              Fast covers twice the distance from slow. If both meet,
 *              then the list is a cycle.
 * Return: 1 if a cycle singly-linked list, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	/* Both nodes point to head */
	slow = fast = list;

	/* If fast is NULL, then there's no cycle */
	while (fast != NULL)
	{
		/* Fast advances twice as fast as slow */
		fast = fast->next;
		/* When fast isn't NULL, then advance both one node */
		if (fast != NULL)
			fast = fast->next, slow = slow->next;
		/*
		 * Eventually fast and slow will meet in a point,
		 * then it will be a cycle.
		 */
		if (fast == slow)
			return (1);
	}
	return (0);
}
