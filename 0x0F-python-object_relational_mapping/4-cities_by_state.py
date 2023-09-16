#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""


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
        "SELECT c.id, c.name, s.name "
        "FROM cities c "
        "JOIN states s ON s.id = c.state_id "
        "ORDER BY c.id ASC"
    )
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import MySQLdb
    import sys
    main(sys.argv)
