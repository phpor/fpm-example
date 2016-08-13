bindir=${bindir-/usr/bin/}
sysconfdir=${sysconfdir-/etc/}
hello:
	cc -o hello hello.c

clean:
	rm -fr hello

install:
	install -d ${bindir} ${sysconfdir}
	install -t ${bindir} hello
	install -t ${sysconfdir} hello.conf

uninstall:
	unlink ${bindir}/hello
	unlink ${sysconfdir}/hello.conf
