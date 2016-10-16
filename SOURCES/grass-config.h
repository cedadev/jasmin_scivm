#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "grass/config-32.h"
#else
#if __WORDSIZE == 64
#include "grass/config-64.h"
#else
#error "Unknown word size"
#endif
#endif
