#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state
"""


def main(args):
    """ All cities by state
    """
    db = MySQLdb.connect(
        host='localhost',
        user=args[1],
        passwd=args[2],
        db=args[3])
    cur = db.cursor()
    query = (
        "SELECT c.name "
        "FROM cities c "
        "JOIN states s ON s.id = c.state_id "
        "WHERE s.name = %s "
        "ORDER BY c.id ASC"
    )
    cur.execute(query, (args[4],))
    states = cur.fetchall()
    print(", ".join(map(lambda x: "%s" % x, states)))


if __name__ == "__main__":
    import MySQLdb
    import sys
    main(sys.argv)
