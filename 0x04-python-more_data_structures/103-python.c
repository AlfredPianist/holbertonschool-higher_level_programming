#include <stdio.h>
#include <strings.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information of a PyBytes object.
 * @p: The PyObject to be analyzed.
 */
void print_python_bytes(PyObject *p)
{
	long int bytes_size, content_limit, i;
	char *content;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &content, &bytes_size);
	content_limit = bytes_size < 9 ? bytes_size + 1 : 10;

	printf("  size: %ld\n", bytes_size);
	printf("  trying string: %s\n", content);
	printf("  first %ld bytes: ", content_limit);
	for (i = 0; i < content_limit - 1; i++)
		printf("%.2hhx ", content[i]);
	printf("%.2hhx\n", content[i]);
}

/**
 * print_python_list - Prints information of a PyList object.
 * @p: The PyObject to be analyzed.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	long int i, list_size;
	PyObject *list_item;
	const char *list_item_type;

	list = (PyListObject *)p;
	list_size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		list_item = PyList_GET_ITEM(list, i);
		list_item_type = (list_item->ob_type)->tp_name;

		printf("Element %ld: %s\n", i, list_item_type);

		if (strcmp(list_item_type, "bytes") == 0)
			print_python_bytes(list_item);
	}
}
