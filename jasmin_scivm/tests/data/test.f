      program nctest
      include 'netcdf.inc'

      integer ncid, ndims, status

      status = nf_open('my.nc', 0, ncid)
      if (status .ne. nf_noerr) call handle_err(status)

      status = nf_inq_ndims(ncid, ndims)
      if (status .ne. nf_noerr) call handle_err(status)

      print *, 'There are ', ndims, 'dimensions'

      status = nf_close(ncid)
      if (status .ne. nf_noerr) call handle_err(status)

      end


      subroutine handle_err(status)
      include 'netcdf.inc'
      integer status
      print *, nf_strerror(status)
      call exit(1)
      end
