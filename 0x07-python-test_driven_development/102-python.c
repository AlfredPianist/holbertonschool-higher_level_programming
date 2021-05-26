#include <stdio.h>
#include <strings.h>
#include <Python.h>

/**
 * print_python_string - Prints information of a string object.
 * @p: The PyObject to be analyzed.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t string_size;
	wchar_t *string_content;
	char *string_type;

	setbuf(stdout, NULL);
	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		string_type = "compact ascii";
	if (PyUnicode_IS_COMPACT(p) && !PyUnicode_IS_ASCII(p))
		string_type = "compact unicode object";

	string_size = PyUnicode_GetLength(p);
	string_content = PyUnicode_AsWideCharString(p, &string_size);

	printf("  type: %s\n", string_type);
	printf("  length: %ld\n", (long int)string_size);
	printf("  value: %ls\n", string_content);
	PyMem_Free(string_content);
}
