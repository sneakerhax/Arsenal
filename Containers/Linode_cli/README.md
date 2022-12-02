# Docker - Linode CLI

A Dockerized version of the Linode CLI

## Running with Docker (Local build)

```
docker build -t linode_cli .
```
Buildling the image

## Run the Linode CLI

```
$ docker run -e LINODE_CLI_TOKEN=$LINODE_CLI_TOKEN -it linode_cli
root@82a3e1e109ca:/# linode-cli account view
┌────────────┬───────────┬──────────────────────┬─────────┬────────────────────┐
│ first_name │ last_name │ email                │ balance │ balance_uninvoiced │
├────────────┼───────────┼──────────────────────┼─────────┼────────────────────┤
│ Ken        | Kaneki    | sneakerhax@gmail.com │ 0.0     │ 100.27             │
└────────────┴───────────┴──────────────────────┴─────────┴────────────────────┘
```
You will need to set the LINODE_CLI_TOKEN in your local env with `export LINODE_CLI_TOKEN=<token>`

## References
* https://www.linode.com/docs/products/tools/cli/guides/install/


