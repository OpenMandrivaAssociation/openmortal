%define	name	openmortal
%define	version	0.7
%define	release %mkrel 12
%define	Summary	Parody of Mortal Kombat

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
#Patch0:	%{name}-0.4-freetype2-compilefix.patch.bz2
Patch:		%{name}-0.7-extra-qualification.patch
License:	GPL
Group:		Games/Arcade
Url:		http://openmortal.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
#BuildRequires:	SDL_ttf-devel
BuildRequires:	freetype2-devel
BuildRequires:	perl-devel

%description
Mortál Szombat is a parody of the popular coin-up game, Mortal Kombat.
It is currently playable (maybe even enjoyable), although it is still
under development. Only two-player game is supported, single-player games
against computer opponent is not planned yet.
There are currently 9 playable characters, and 8 more in the making!

%prep
%setup -q
#%patch0 -p1
%patch -p0

%build
%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std

%{__install} -d $RPM_BUILD_ROOT%{_menudir}
%{__cat} <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		icon=%{name}.png \
		needs="x11" \
		section="More Applications/Games/Arcade" \
		title="Mortal Szombat" \
		longtitle="%{Summary}" \
		xdg="true"
EOF

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

%{__install} %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL PACKAGERS README TODO
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
