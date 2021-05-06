#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *list_item;
	long int i, size;

	list = (PyListObject *)p;
	size = (long int)PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		list_item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(list_item)->tp_name);
	}
}
