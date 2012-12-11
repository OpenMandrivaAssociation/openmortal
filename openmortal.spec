%define	name openmortal
%define	version 0.7.1
%define sversion 0.7
%define	release 6
%define	summary Parody of Mortal Kombat

Summary: %{summary}
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{sversion}.tar.bz2
Source1: laurence.zip
Source2: ikari.zip
Source11: %{name}-16x16.png
Source12: %{name}-32x32.png
Source13: %{name}-48x48.png
#Patch0: %{name}-0.4-freetype2-compilefix.patch.bz2
Patch: %{name}-0.7-extra-qualification.patch
License: GPL
Group: Games/Arcade
Url: http://openmortal.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_net-devel
BuildRequires: SDL_ttf-devel
BuildRequires: freetype2-devel
BuildRequires: perl-devel

%description
Open Mortal is a parody of the popular coin-up game, Mortal Kombat.
It is currently playable (maybe even enjoyable), although it is still
under development. Only two-player game is supported, single-player games
against computer opponent is not planned yet.
There are currently 9 playable characters, and 8 more in the making!

%prep
%setup -n %{name}-%{sversion} -q
#%patch0 -p1
%patch -p0
unzip %{SOURCE1} -d data/gfx
unzip %{SOURCE2} -d data/gfx

#perl -pi -e "s|level6.jpg|level6.jpg level12.desc level12_arena.png\
# level12_background.png level12_left.png level12_right.png level13.desc\
# level13_arena.png level13_background.png level13_plane2.png|"\
# data/gfx/Makefile.in

%build
%configure --bindir=%{_gamesbindir} \
 --datadir=%{_gamesdatadir}

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Open Mortal
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%{__install} %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
%{__install} %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
%{__install} %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL PACKAGERS README TODO
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Sun Nov 20 2011 Sergio Rafael Lemke <sergio@mandriva.com> 0.7.1-6
+ Revision: 731912
- Rebuild against new perl, some changes to make it build

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-5mdv2011.0
+ Revision: 613539
- rebuild

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 0.7.1-4mdv2010.1
+ Revision: 541472
- fix desktop file

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-4mdv2010.0
+ Revision: 430212
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.7.1-3mdv2009.0
+ Revision: 254841
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Guillaume Bedot <littletux@mandriva.org> 0.7.1-1mdv2008.1
+ Revision: 179305
- 0.7.1 (two new backgrounds)

* Fri Jan 25 2008 Guillaume Bedot <littletux@mandriva.org> 0.7-13mdv2008.1
+ Revision: 157730
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun May 20 2007 Olivier Thauvin <nanardon@mandriva.org> 0.7-12mdv2008.0
+ Revision: 28819
- rebuild: mkrel size does matter


* Sun Dec 31 2006 Olivier Blin <oblin@mandriva.com> 0.7-11mdv2007.0
+ Revision: 102970
- buildrequires freetype2-devel

  + Olivier Thauvin <nanardon@mandriva.org>
    - rebuild
    - Import openmortal

* Fri Jun 30 2006 Guillaume Bedot <littletux@mandriva.org> 0.7-10mdv2007.0
- rebuilt for perl 5.8.8.
- %%mkrel
- XDG menu
- gcc 4.1 patch (extra qualification)

* Sat May 21 2005 Guillaume Bedot <littletux@mandriva.org> 0.7-9mdk
- rebuilt for perl 5.8.7.

* Wed May 18 2005 Guillaume Bedot <littletux@mandriva.org> 0.7-8mdk
- removed vendor hardcoded in the spec, thanks stew_b.
- /me needs brain and smaller fingers.

* Wed May 18 2005 Guillaume Bedot <littletux@mandriva.org> 0.7-7777777removed vendor hardcoded in the spec, thanks stew_b.
* Tue May 17 2005 Guillaume Bedot <littletux@mandriva.org> 0.7-6mdk
- fixed wrong rights on doc.

* Mon May 16 2005 Guillaume Bedot <littletux@mandriva.org> 0.7-5mdk
- fixed menu section
- fixed missing doc

* Sun May 15 2005 Guillaume Bedot <littletux@mandriva.org> 0.7-4mdk
- rebuilt to run on cooker / LE 2005 again.
 ( i apologize for this, i uploaded to the wrong plf section, but it finally
 appeared that it was wrong for this package to be in plf... )
- it appears that openmortal data is free to distribute, so this package 
 goes to contribs.

* Sun Apr 03 2005 Guillaume Bedot <littletux@zarb.org> 0.7-3plf
- rebuilt to run on cooker / LE 2005.

* Wed Aug 25 2004 Guillaume Rousse <guillomovitch@zarb.org> 0.7-2plf
- rebuild for new perl

* Sun May 16 2004 Olivier Blin <blino@mandrake.org> 0.7-1plf
- fix menu entry
- 0.7

* Tue Apr 27 2004 Stefan van der Eijk <stefan@zarb.org> 0.6-2plf
- BuildRequires

* Wed Mar 17 2004 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.6-1plf
- 0.6

* Fri Feb 06 2004 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.5-1plf
- 0.5
- drop P0

* Mon Jan 12 2004 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.4-1plf
- 0.4
- fix build with newer freetype (P0)

