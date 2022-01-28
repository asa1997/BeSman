#!/bin/bash

function __besman_check_oah_exists
{
    if [[ -z $OAH_DIR ]]; then
        __besman_echo_red "OAH not installed. Please install OAH and run again"
        return 1
    else
        return 0
    fi
}   

function __besman_oah_install_on_host
{
    local environment=$1
    oah install -s $environment
    unset environment
}

function __besman_set_oah_env_clone
{
    local val=$1
    [[ $val == "false" ]] && export OAH_ENV_CLONE=false
    [[ $val == "true" ]] && export OAH_ENV_CLONE=true
    unset val
}

function __besman_source_init
{
    [[ ! -f $OAH_DIR/bin/oah-init.sh ]] && __besman_echo_red "Could not init OAH. File not found" && return 1

    source $OAH_DIR/bin/oah-init.sh
}

function __besman_open_vm_config
{
    local file_path=$1
    nano $file_path
    unset file_path
}
