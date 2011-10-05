SUBDIRS = bin plauncher data

INTLTOOL = 			\
	intltool-extract.in 	\
	intltool-merge.in 	\
	intltool-update.in

desktopdir = $(datadir)/applications
desktop_in_files=plauncher.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)
@INTLTOOL_DESKTOP_RULE@

EXTRA_DIST =  \
	$(desktop_in_files) \
	$(desktop_DATA) \
	pyreqs.py \
	$(INTLTOOL) 

DISTCHECK_CONFIGURE_FLAGS = --disable-scrollkeeper
DISTCLEANFILES = \
	$(desktop_DATA) \
	intltool-extract \
	intltool-merge \
	intltool-update	

