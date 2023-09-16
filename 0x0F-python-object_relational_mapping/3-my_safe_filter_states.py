#!/usr/bin/python3
"""gets all states via python
"""


def main(args):
    """gets all state
    """
    db = MySQLdb.connect(
        host='localhost',
        user=args[1],
        passwd=args[2],
        db=args[3])
    cur = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY %s "
        "ORDER BY id ASC"
    )
    cur.execute(query, (args[4] + '%',))
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import MySQLdb
    import sys
    main(sys.argv)
