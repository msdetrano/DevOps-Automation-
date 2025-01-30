#!/bin/bash

DIR_ORIGEM="/home/user/projetos"
DIR_BACKUP="/backup"
ARQUIVO_BACKUP="backup_$(date +%Y%m%d%H%M%S).tar.gz"

tar -czf "$DIR_BACKUP/$ARQUIVO_BACKUP" "$DIR_ORIGEM"

echo "Backup salvo em: $DIR_BACKUP/$ARQUIVO_BACKUP"
