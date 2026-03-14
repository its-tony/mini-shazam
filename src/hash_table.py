import math

from matplotlib.typing import CapStyleType

"""
Custom hash table with separate chaining.

This is the CORE data structure for the Mini Shazam project.
You must implement this from scratch — no built-in dicts or hashmaps allowed.

Refer to GUIDE.md, Milestone 1 for detailed instructions.
"""


class HashTable:
    """
    Hash table using separate chaining.

    Each bucket is a Python list of (key, value) pairs.
    When multiple entries hash to the same bucket, they form a "chain."

    You will implement:
      - _hash(key)       : Map an integer key to a bucket index
      - insert(key, value): Add a (key, value) pair to the table
      - lookup(key)       : Retrieve all values associated with a key
      - size()            : Return the total number of stored entries
      - capacity()        : Return the number of buckets
      - load_factor()     : Return entries / capacity
      - stats()           : Return collision statistics as a dict
      - _next_prime(n)    : Find the smallest prime >= n
      - _resize()         : Double capacity and rehash all entries
    """

    DEFAULT_CAPACITY = 10007  # A prime number — why prime? See GUIDE.md

    def __init__(self, capacity=None):
        self._capacity = capacity or self.DEFAULT_CAPACITY
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    # ------------------------------------------------------------------ #
    # Hash function
    # ------------------------------------------------------------------ #

    def _hash(self, key):
        """
        Map an integer key to a bucket index in range [0, capacity).

        Requirements:
          - Must return an integer in [0, self._capacity)
          - Must be deterministic (same key always maps to same index)
          - Should distribute keys uniformly across buckets

        Hint: The Knuth multiplicative hash works well here.
              Multiply the key by a large constant, then take modulo capacity.
              The constant 2654435761 (a prime close to 2^32 * phi) is a
              classic choice from Knuth's "The Art of Computer Programming."

        Important: Use int(key) to convert the key to a Python int first.
                   This avoids integer overflow issues with numpy int64 values.

        Args:
            key: An integer hash key

        Returns:
            An integer bucket index in [0, self._capacity)
        """
        raise NotImplementedError("_hash not implemented yet.")

    # ------------------------------------------------------------------ #
    # Core operations
    # ------------------------------------------------------------------ #

    def insert(self, key, value):
        """
        Insert a (key, value) pair into the hash table.

        Steps:
          1. Compute the bucket index using self._hash(key)
          2. Append the (key, value) tuple to that bucket's list
          3. Increment self._size
          4. Check if load_factor() > 0.75 — if so, call self._resize()

        Note: Duplicate keys ARE allowed. In Shazam, many different songs
        can produce the same fingerprint hash, so the same key may have
        multiple values. This is why each bucket is a list, not a single slot.

        Args:
            key: The hash key (an integer)
            value: The value to store (in our case, a (song_id, time_offset) tuple)
        """
        raise NotImplementedError("insert not implemented yet.")

    def lookup(self, key):
        """
        Return a list of ALL values associated with the given key.

        Steps:
          1. Compute the bucket index using self._hash(key)
          2. Iterate through the bucket's chain (list of (key, value) pairs)
          3. Collect all values where the stored key matches the query key
          4. Return the list (empty list if no matches)

        Why return ALL values? In Shazam, the same fingerprint hash can
        appear in multiple songs (or at multiple positions in the same song).
        We need all of them to do proper time-coherent matching later.

        Args:
            key: The hash key to look up

        Returns:
            A list of values associated with this key (may be empty)
        """
        raise NotImplementedError("lookup not implemented yet.")

    # ------------------------------------------------------------------ #
    # Size & statistics
    # ------------------------------------------------------------------ #

    def size(self):
        """Return the total number of stored entries."""
        raise NotImplementedError("size not implemented yet.")

    def capacity(self):
        """Return the current number of buckets."""
        raise NotImplementedError("capacity not implemented yet.")

    def load_factor(self):
        """
        Return the load factor: entries / capacity.

        The load factor tells you how "full" the table is.
        - 0.0 means empty
        - 0.5 means half the buckets have one entry (on average)
        - 1.0 means as many entries as buckets
        - > 1.0 means chains are getting long on average

        We resize when this exceeds 0.75 to keep lookups fast.
        """
        raise NotImplementedError("load_factor not implemented yet.")

    def stats(self):
        """
        Return a dictionary of collision statistics.

        This is useful for analyzing how well your hash function distributes keys.

        Must return a dict with these keys:
          - "capacity": current number of buckets
          - "size": total number of stored entries
          - "load_factor": entries / capacity (rounded to 4 decimal places)
          - "empty_buckets": number of buckets with no entries
          - "max_chain_length": length of the longest chain
          - "avg_chain_length": average length of non-empty chains (rounded to 4 decimal places)

        Returns:
            dict with the keys described above
        """
        raise NotImplementedError("stats not implemented yet.")

    # ------------------------------------------------------------------ #
    # Resizing
    # ------------------------------------------------------------------ #

    @staticmethod
    def _next_prime(n):
        """
        Find the smallest prime number >= n.

        This is used during resizing: we double the capacity and then
        find the next prime to use as the new capacity. Prime capacities
        help distribute keys more evenly (especially with modular hashing).

        Algorithm:
          1. If n <= 2, return 2
          2. Start with candidate = n (or n+1 if n is even)
          3. Test if candidate is prime by checking divisibility
             by all odd numbers from 3 to sqrt(candidate)
          4. If not prime, increment by 2 and try again

        Args:
            n: The minimum value for the prime

        Returns:
            The smallest prime >= n
        """
        raise NotImplementedError("_next_prime not implemented yet.")

    def _resize(self):
        """
        Double the capacity (to the next prime) and rehash all entries.

        Steps:
          1. Compute new capacity = _next_prime(self._capacity * 2)
          2. Save the old buckets
          3. Reset self._capacity, self._buckets, and self._size
          4. Re-insert every (key, value) pair from the old buckets

        Why is this necessary? As the load factor increases, chains get
        longer and lookups slow down from O(1) toward O(n). Resizing
        keeps chains short.

        What is the time complexity of this operation? How often does it
        happen? What is the amortized cost per insertion? (Think about this!)
        """
        raise NotImplementedError("_resize not implemented yet.")
