#!/bin/bash
src_dir=$1
dst_dir=$2
echo $dst_dir
mkdir -p lib/php/extensions/no-debug-non-zts-20151012/  bin sbin etc/init.d etc/php-fpm.d etc/php.d man/man1 man/man8 include
cd $src_dir
cp sapi/cli/php $dst_dir/bin/
cp sapi/cli/php.1 $dst_dir/man/man1/
cp sapi/phpdbg/phpdbg.1 $dst_dir/man/man1/
cp sapi/cgi/php-cgi.1 $dst_dir/man/man1/
cp sapi/fpm/php-fpm.8 $dst_dir/man/man8/
cp sapi/fpm/php-fpm.conf $dst_dir/etc/
cp sapi/fpm/init.d.php-fpm $dst_dir/etc/init.d/php-fpm
cp sapi/cgi/php-cgi $dst_dir/bin/
cp sapi/php-fpm/php-fpm $dst_dir/sbin/
cp sapi/phpdbg/phpdbg $dst_dir/bin/
cp sapi/fpm/php-fpm $dst_dir/sbin/
cp scripts/phpize $dst_dir/bin/
cp scripts/php-config $dst_dir/bin/
cp scripts/man1/php-config.1 $dst_dir/man/man1/
cp scripts/man1/phpize.1 $dst_dir/man/man1/
