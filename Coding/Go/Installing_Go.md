# Installing Go (OSX)

**Description:** This entry describes how to install and configure Go on OSX

**Requirements:** brew (optional)

## Installation

* Install [Go](https://go.dev/doc/install)
* Install [GO with Brew](https://formulae.brew.sh/formula/go)

```
brew install go
```

Install Go using brew

```
export GOPATH="$HOME/go"
export PATH="$GOPATH/bin:$PATH"
```

Set gopath and append gobin path so that packages installed with go install can be located by your terminal (add to .zshrc for persistence)
  
## References
* [Get Started](https://go.dev/learn/)
* [Go documentation](https://go.dev/doc/)
