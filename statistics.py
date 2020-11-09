from app import statDB

# Update the statistics after a new message is sent.
def update_statistics(msg):
    # Update workspace-wide statistics
    prev_stats = statDB.read_item(item="1")
    prev_stats['total_workspace_messages'] += 1
    statDB.upsert_item(prev_stats)

    # Update individual user statistics

    # Update individual channel statistics

    return
