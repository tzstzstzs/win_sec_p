def sort_by(tree, column, sort_order, ascending_symbol=" ▲", descending_symbol=" ▼"):
    """
    Generalized sort function for treeview columns.

    :param tree: The treeview object.
    :param column: The column to sort by.
    :param sort_order: Dictionary containing the order of sorting for each column.
    :param ascending_symbol: Symbol to indicate ascending sort.
    :param descending_symbol: Symbol to indicate descending sort.
    """
    # Toggle sort order for the column
    order = sort_order.get(column, True)  # Default to ascending if not set

    # Retrieve and sort the data
    data = [(tree.set(k, column), k) for k in tree.get_children('')]
    try:
        data.sort(key=lambda t: int(t[0]), reverse=order)
    except ValueError:
        data.sort(key=lambda t: t[0], reverse=order)

    # Update the treeview with sorted data
    for index, (_, k) in enumerate(data):
        tree.move(k, '', index)

    # Update headers with arrow symbols
    for c in sort_order.keys():
        header = c
        if c == column:
            header += ascending_symbol if order else descending_symbol

        tree.heading(c, text=header)

    # Toggle and return the updated sort order
    sort_order[column] = not order
    return sort_order
