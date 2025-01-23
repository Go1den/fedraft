def get(draftPicks):
    return [
        ('0xCC5B50', draftPicks[0].id),
        ('0xCC5B51', draftPicks[0].supportClass),
        ('0xCC5B58', draftPicks[0].heldItems.item1),
        ('0xCC5B59', draftPicks[0].heldItems.item2),
        ('0xCC5B5A', draftPicks[0].heldItems.item3),
        ('0xCC5B5B', draftPicks[0].heldItems.item4)
    ]