Name:           geogebra-oxygen-icons
Summary:        GeoGebra Icons for Oxygen Icon Theme
Version:        0.18.1
Release:        %mkrel 1
Group:          Sciences/Mathematics
License:        LGPLv3
Source:         GeoGebra_oxygen_icons.tar.gz
Requires:       oxygen-icon-theme
%if !0%{?fedora} && !0%{?rhel_version} && !0%{?centos_version}
Supplements:    packageand(geogebra-thumbnail-kde:oxygen-icon-theme)
Supplements:    packageand(mimehandler(application/vnd.geogebra.file):oxygen-icon-theme)
Supplements:    packageand(mimehandler(application/vnd.geogebra.tool):oxygen-icon-theme)
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides MIME type icons that integrate well into the KDE/Oxygen icon theme (http://www.oxygen-icons.org).

%prep
%setup -q -n GeoGebra_oxygen_icons

%build
#

%install
rm -rf %{buildroot}
for SIZE in 16x16 22x22 32x32 48x48 64x64 128x128 256x256; do
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/oxygen/$SIZE/mimetypes
%{__install} -m644 oxygen/$SIZE/mimetypes/application-vnd.geogebra.file.png %{buildroot}%{_datadir}/icons/oxygen/$SIZE/mimetypes
%{__install} -m644 oxygen/$SIZE/mimetypes/application-vnd.geogebra.tool.png %{buildroot}%{_datadir}/icons/oxygen/$SIZE/mimetypes
done
%{__install} -d -m755 %{buildroot}%{_docdir}/%{name}
%{__install} -m644 COPYING %{buildroot}%{_docdir}/%{name}/
%{__install} -m644 README %{buildroot}%{_docdir}/%{name}/

%clean
rm -rf %{buildroot}

%post
%if 0%{?mandriva_version}
%update_icon_cache oxygen
%endif

%postun
%if 0%{?mandriva_version}
%update_icon_cache oxygen
%endif

%files
%defattr(-,root,root)
%dir %{_datadir}/icons/oxygen
%dir %{_datadir}/icons/oxygen/16x16
%dir %{_datadir}/icons/oxygen/22x22
%dir %{_datadir}/icons/oxygen/32x32
%dir %{_datadir}/icons/oxygen/48x48
%dir %{_datadir}/icons/oxygen/64x64
%dir %{_datadir}/icons/oxygen/128x128
%dir %{_datadir}/icons/oxygen/256x256
%dir %{_datadir}/icons/oxygen/16x16/mimetypes
%dir %{_datadir}/icons/oxygen/22x22/mimetypes
%dir %{_datadir}/icons/oxygen/32x32/mimetypes
%dir %{_datadir}/icons/oxygen/48x48/mimetypes
%dir %{_datadir}/icons/oxygen/64x64/mimetypes
%dir %{_datadir}/icons/oxygen/128x128/mimetypes
%dir %{_datadir}/icons/oxygen/256x256/mimetypes
%{_docdir}/%{name}
%{_datadir}/icons/oxygen/*/*/*.png

