# Reducing the size of Go binaries

**Description:** This entry describes how to reduce the size of Go binaries that are typically larger than other compiled binaries. This is because all dependencies are packed into the binary

**Requirements:** go, upx

## Reducing binary size

```
go build -ldflags="-s -w" <file.go>
```

Use linker flags to strip debugging information

```
upx --brute <binary>
```

Pack the binary with UPX

## References
* https://blog.filippo.io/shrink-your-go-binaries-with-this-one-weird-trick/
* https://formulae.brew.sh/formula/upx
