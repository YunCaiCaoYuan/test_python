#include <Python.h>

int main(int argc, char *argv[]) {
  Py_Initialize();
  PyRun_SimpleString("print('hello world')\n");
  Py_Finalize();
  return 0;
}
// g++ main.cpp -I$PYTHON_PATH/include/python2.7 -lpython2.7
// 输出 hello world
