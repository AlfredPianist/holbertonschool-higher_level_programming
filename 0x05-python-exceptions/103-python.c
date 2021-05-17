#include <stdio.h>
#include <strings.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

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

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	list_size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		list_item = PyList_GET_ITEM(list, i);
		list_item_type = (list_item->ob_type)->tp_name;

		printf("Element %ld: %s\n", i, list_item_type);

		if (strcmp(list_item_type, "bytes") == 0)
			print_python_bytes(list_item);
		if (strcmp(list_item_type, "float") == 0)
			print_python_float(list_item);
	}
}

/**
 * print_python_bytes - Prints information of a PyBytes object.
 * @p: The PyObject to be analyzed.
 */
void print_python_bytes(PyObject *p)
{
	PyVarObject *bytes_var;
	PyBytesObject *bytes;
	long int bytes_size, content_limit, i;
	char *content;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes_var = (PyVarObject *)p;
	bytes_size = bytes_var->ob_size;
	content_limit = bytes_size < 9 ? bytes_size + 1 : 10;

	bytes = (PyBytesObject *)p;
	content = bytes->ob_sval;

	printf("  size: %ld\n", bytes_size);
	printf("  trying string: %s\n", content);

	printf("  first %ld bytes: ", content_limit);
	for (i = 0; i < content_limit - 1; i++)
		printf("%.2hhx ", content[i]);
	printf("%.2hhx\n", content[i]);
}

/**
 * print_python_float - Prints information of a PyFloat object.
 * @p: The PyObject to be analyzed.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_object;
	double float_number;
	char *float_string;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_object = (PyFloatObject *)p;
	float_number = float_object->ob_fval;
	float_string = PyOS_double_to_string(float_number, 'r', 0,
					     Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", float_string);
	PyMem_Free(float_string);
}
