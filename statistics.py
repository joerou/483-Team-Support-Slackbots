# Update the statistics after a new message is sent.
def update_statistics(msg, statDB):
    # Update workspace-wide statistics
    prev_stats = statDB.read_item(item="1", partition_key="Workspace-wide stats")
    prev_stats['total_workspace_messages'] += 1
    statDB.replace_item("1", prev_stats)

    # Update individual user statistics

    # Update individual channel statistics

    return
