Summary:	gQueue is a GNOME2 frontend for Cups queues
Summary(pl):	gQueue jest nak³adk± na Cupsa dla GNOME2
Name:		gqueue
Version:	0.99.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://web.tiscali.it/diegobazzanella/%{name}-%{version}.tar.bz2
# Source0-md5:	b5cf07a087986cd4cbb83ed26958d408
Source1:	%{name}.desktop
Patch0:		%{name}-locale.patch
URL:		http://web.tiscali.it/diegobazzanella/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libbonoboui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0.1
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.1-13
Requires:	cups
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gQueue is a GNOME2 frontend for lpq and lprm working with Cups queues.

%description -l pl
gQueue jest nak³adk± na lpq i lprm pracuj±c± z kolejkami Cupsa.

%prep
%setup -q -n %{name}
%patch0 -p1

mv po/{no,nb}.po

%build
rm -f missing mkinstalldirs depcomp install-sh missing COPYING INSTALL
cp /usr/share/gettext/mkinstalldirs .
%{__aclocal}
glib-gettextize --force --copy
%{__autoheader}
%{__automake} --add-missing
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
