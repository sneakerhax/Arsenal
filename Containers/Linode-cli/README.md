# Docker - Linode CLI

A Dockerized version of the Linode CLI

## Running with Docker (Local build)

```
docker build -t linode_cli .
```
Buildling the image

## Run the Linode CLI

```
$ docker run -e LINODE_CLI_TOKEN=$LINODE_CLI_TOKEN -it linode-cli account view
┌────────────┬───────────┬──────────────────────┬─────────┬────────────────────┐
│ first_name │ last_name │ email                │ balance │ balance_uninvoiced │
├────────────┼───────────┼──────────────────────┼─────────┼────────────────────┤
│ Ken        | Kaneki    | sneakerhax@gmail.com │ 0.0     │ 100.27             │
└────────────┴───────────┴──────────────────────┴─────────┴────────────────────┘
```
You will need to set the LINODE_CLI_TOKEN in your local env with `export LINODE_CLI_TOKEN=<token>`

## Usage Examples

```
linode-cli account view
```

List account information

```
linode-cli linodes list
```

List all computer instances

```
linode-cli stackscripts list --mine true
```

List the StackScripts created by you.

## References
* https://www.linode.com/docs/products/tools/cli/guides/install/


