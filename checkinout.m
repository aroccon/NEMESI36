clear all
nx=64;
ny=nx;
dx=2*pi/(nx-1);
dxi=1/dx;

fid = fopen('outr.dat');
var = fread(fid, (nx/2+1)*ny, 'double');
fclose(fid);
outr=reshape(var,[nx/2+1 ny]);

fid = fopen('outi.dat');
var = fread(fid, (nx/2+1)*ny, 'double');
fclose(fid);
outi=reshape(var,[nx/2+1 ny]);


figure(2)
clf
subplot(1,2,1)
hold on
surf(outr)
colorbar
hold off

subplot(1,2,2)
hold on
surf(outi)
colorbar
hold off


