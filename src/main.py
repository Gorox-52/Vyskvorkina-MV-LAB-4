#!/usr/bin/env python3
"""
Главный файл для запуска симуляции библиотеки.
Лабораторная работа №4: Симуляция с пользовательскими коллекциями
Вариант 1: «Библиотека»
"""

import sys
from simulation import LibrarySimulator

def main():
    
    simulator = LibrarySimulator()
    
    steps = 20
    seed = 52
    
    print(f"  • Количество шагов: {steps}")
    print(f"  • Seed: {seed if seed else 'случайный'}")
    
    print("\n" + "=" * 60)
    print("НАЧАЛО СИМУЛЯЦИИ")
    print("=" * 60)
    
    try:
        simulator.run_simulation(steps=steps, seed=seed)
    except KeyboardInterrupt:
        print("\n\nСимуляция прервана пользователем.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nОшибка во время симуляции: {e}")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("СИМУЛЯЦИЯ ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 60)

if __name__ == "__main__":
        main()