# Homebrew proper setup
sudo chown -R $(whoami) /usr/local/etc /usr/local/include /usr/local/lib /usr/local/lib/pkgconfig /usr/local/share
chmod u+w /usr/local/etc /usr/local/include /usr/local/lib /usr/local/lib/pkgconfig /usr/local/share


# Install httppie
brew install httpie
