SUBDIRS = bin ginfotweaks data po  
INTLTOOL = 			\
	intltool-extract.in 	\
	intltool-merge.in 	\
	intltool-update.in

desktopdir = $(datadir)/applications
desktop_in_files=ginfotweaks.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)
@INTLTOOL_DESKTOP_RULE@

EXTRA_DIST =  \
	$(desktop_in_files) \
	$(desktop_DATA) \
	gnome-doc-utils.make \
	$(INTLTOOL) 

DISTCHECK_CONFIGURE_FLAGS = \
        --disable-scrollkeeper \
	--enable-pydoc

DISTCLEANFILES = \
	$(desktop_DATA) \
	intltool-extract \
	intltool-merge \
	intltool-update	\
	gnome-doc-utils.make

