%define	name openmortal
%define	version 0.7.1
%define sversion 0.7
%define	release %mkrel 1
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
#BuildRequires: SDL_ttf-devel
BuildRequires: freetype2-devel
BuildRequires: perl-devel

%description
Mortál Szombat is a parody of the popular coin-up game, Mortal Kombat.
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
perl -pi -e "s|level6.jpg|level6.jpg level12.desc level12_arena.png\
 level12_background.png level12_left.png level12_right.png level13.desc\
 level13_arena.png level13_background.png level13_plane2.png|"\
 data/gfx/Makefile.in


%build
%configure --bindir=%{_gamesbindir} \
 --datadir=%{_gamesdatadir}

%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Mortal Szombat
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%{__install} %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
%{__install} %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
%{__install} %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf %{buildroot}

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
