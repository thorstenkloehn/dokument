Hier ist eine Liste neuer Programmiersprachen. Sie sollen erst erwachsene Werte wie C++, C# und Java erreichen.
### Rust Installieren
Rust ist noch eine wachsende Programmiersprache, weil sie sich noch in der Entwicklung befindet und ständig neue Funktionen und Verbesserungen erhält. Sie bietet jedoch bereits jetzt viele Vorteile wie Speicher- und Thread-Sicherheit, was sie zu einer vielversprechenden Wahl für moderne Softwareentwicklung macht.
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
code --install-extension rust-lang.rust-analyzer
```
### Golang Installieren
Golang bietet ein umfangreiches und sicheres Standardpaket für die Webentwicklung. Leider sind externe Datenbanktreiber sowie externe Bibliotheken und Frameworks nicht stabil genug, um sie sicher in Produktionsumgebungen zu nutzen.

```bash
cd $HOME
wget https://go.dev/dl/go1.24.1.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.24.1.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc
```
### Emscripten Installieren
```
sudo apt install emscripten
```