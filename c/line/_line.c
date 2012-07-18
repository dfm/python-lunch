#include <Python.h>
#include <numpy/arrayobject.h>

#include "line.h"

/* Docstrings are good! */
static char module_docstring[] = "Fit a line to some data.";

static char lnlike_docstring[] =
                "Calculate the log-likelihood of some data given a model.";

/* Declare the C functions here. */
static PyObject *line_lnlike(PyObject *self, PyObject *args);

/* Define the methods that will be available on the module. */
static PyMethodDef module_methods[] = {
    {"lnlike", line_lnlike, METH_VARARGS, lnlike_docstring},
    {NULL, NULL, 0, NULL}
};

/* This is the function that is called on import. */
PyMODINIT_FUNC init_line(void)
{
    /* Initialize the module with a docstring. */
    PyObject *m = Py_InitModule3("_line", module_methods, module_docstring);
    if (m == NULL)
        return;

    /* Load all of the `numpy` functionality. */
    import_array();
}

/* Do the heavy lifting here */
static PyObject *line_lnlike(PyObject *self, PyObject *args)
{
    double m, b;
    PyObject *x_obj, *y_obj, *yerr_obj;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "ddOOO", &m, &b, &x_obj, &y_obj, &yerr_obj))
        return NULL;

    /* Interpret the input objects as `numpy` arrays. */
    PyObject *x_array = PyArray_FROM_OTF(x_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *y_array = PyArray_FROM_OTF(y_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *yerr_array = PyArray_FROM_OTF(yerr_obj, NPY_DOUBLE, NPY_IN_ARRAY);

    /* If that didn't work, throw an `Exception`. */
    if (x_array == NULL || y_array == NULL || yerr_array == NULL) {
        PyErr_SetString(PyExc_TypeError, "Couldn't parse the input arrays.");
        Py_XDECREF(x_array);
        Py_XDECREF(y_array);
        Py_XDECREF(yerr_array);
        return NULL;
    }

    /* How many data points are there? */
    int N = (int)PyArray_DIM(x_array, 0);

    /* Check the dimensions. */
    if (N != (int)PyArray_DIM(y_array, 0)
            || N != (int)PyArray_DIM(yerr_array, 0)) {
        PyErr_SetString(PyExc_RuntimeError, "Dimension mismatch.");
        Py_DECREF(x_array);
        Py_DECREF(y_array);
        Py_DECREF(yerr_array);
        return NULL;
    }

    /* Get pointers to the data as C-types. */
    double *x    = (double*)PyArray_DATA(x_array);
    double *y    = (double*)PyArray_DATA(y_array);
    double *yerr = (double*)PyArray_DATA(yerr_array);

    /* Compute the log-likelihood using an external function. */
    double chi2 = compute_chi2(m, b, x, y, yerr, N);

    /* Clean up. */
    Py_DECREF(x_array);
    Py_DECREF(y_array);
    Py_DECREF(yerr_array);

    /* Build the output tuple */
    PyObject *ret = Py_BuildValue("d", -0.5 * chi2);
    if (ret == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "Couldn't build output.");
        return NULL;
    }

    return ret;
}
