#include <Python.h>
/**
 * print_python_list - this function prints the lists that are going to be
 *                     the main program
 * @p: ...
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
/**
 *print_python_bytes - ...
 * @p: ...
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid PyBytesObject\n");
		return;
	}
	Py_ssize_t size = PyBytes_GET_SIZE(p);
	char *bytes = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	printf("  first %ld bytes: ", (size < 10) ? size : 10);
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", bytes[i]);
		if (i < 9 && i + 1 < size && i + 1 < 10)
			printf(" ");
	}
	printf("\n");
}
/**
 * print_python_float - ...
 * @p: ...
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid PyFloatObject\n");
		return;
	}
	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
