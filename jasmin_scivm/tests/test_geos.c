#include <geos_c.h>

int main()
{
  GEOSGeometry *g1, *g2;
  GEOSContextHandle_t handle;
  GEOSWKTReader *wktReader;
  double dist;
  handle = initGEOS_r(NULL, NULL);

  wktReader = GEOSWKTReader_create_r(handle);

  g1 = GEOSWKTReader_read_r(handle, wktReader, "POINT(10 10)");
  g2 = GEOSWKTReader_read_r(handle, wktReader, "POINT(3 6)");

  GEOSDistance_r(handle, g1, g2, &dist);
}
