import sys
input = sys.stdin.readline

num_cases = int(input())
for case in range(1, num_cases + 1):
    line = input().strip()
    if not line:
        line = input().strip()
    num_warriors, num_sorcerers, available_magic_powder, _ = map(int, line.split())

    spell_limit_per_warrior = []
    accepted_spells_per_warrior = []
    for _ in range(num_warriors):
        parts = list(map(int, input().split()))
        spell_limit, num_spells, *spells = parts
        spell_limit_per_warrior.append(spell_limit)
        accepted_spells_per_warrior.append(set(spells))
    
    castable_spells = set()
    for _ in range(num_sorcerers):
        parts = list(map(int, input().split()))
        num_spells, *spells = parts
        castable_spells.update(spells)
    
    total_requested_spells = sum(
        spell_limit for spell_limit, allowed in zip(spell_limit_per_warrior, accepted_spells_per_warrior)
        if allowed & castable_spells
    )
    result = min(available_magic_powder, total_requested_spells)
    print(f"Case #{case}: {result}")