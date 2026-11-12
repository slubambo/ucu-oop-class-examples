from abc import ABC, abstractmethod

# =====================================================================
# BASE CLASS (Parent for Inheritance)
# =====================================================================
class MasterPerformer(ABC):
    """Abstract base class establishing foundational attributes for all artists."""
    def __init__(self, artist_name, stage_category):
        self.artist_name = artist_name
        self.stage_category = stage_category

    def display_artist_info(self):
        """Common inherited method available to Epaja."""
        print(f"[MasterPerformer Info]: Artist -> {self.artist_name} | Category -> {self.stage_category}")

    @abstractmethod
    def perform_act(self):
        """Abstract method that forces subclasses to implement polymorphism."""
        pass


# =====================================================================
# EPAJA'S CLASS (Combining Inheritance, Encapsulation, and Polymorphism)
# =====================================================================
class EpajaTalentAct(MasterPerformer):
    """
    Epaja's class demonstrates 3 core OOP properties:
    1. INHERITANCE (inherits from MasterPerformer)
    2. ENCAPSULATION (protects private attributes with property decorators)
    3. POLYMORPHISM (overrides perform_act() with custom behavior)
    """
    def __init__(self, artist_name, stage_category, primary_talent, initial_energy=85):
        # --- OOP PROPERTY 1: INHERITANCE ---
        # Calling super().__init__() to inherit attributes from MasterPerformer
        super().__init__(artist_name, stage_category)
        
        self.primary_talent = primary_talent
        
        # --- OOP PROPERTY 2: ENCAPSULATION ---
        # Private attributes (prefixed with double underscores '__') 
        # to restrict unauthorized direct modification from outside the class.
        self.__energy_level = initial_energy
        self.__secret_prop_code = "EPAJA-PROP-9942"

    # =================================================================
    # ENCAPSULATION: GETTERS AND SETTERS USING PYTHON PROPERTIES
    # =================================================================
    @property
    def energy_level(self):
        """Getter property to safely read Epaja's private energy level."""
        return self.__energy_level

    @energy_level.setter
    def energy_level(self, new_energy):
        """Setter property with validation logic to protect the internal state."""
        if 0 <= new_energy <= 100:
            self.__energy_level = new_energy
            print(f"[Encapsulation Update]: Epaja's energy level successfully updated to {self.__energy_level}%.")
        else:
            print("[Encapsulation Error]: Energy level must be between 0 and 100!")

    @property
    def secret_prop_code(self):
        """Getter property for the secret prop code (read-only protection)."""
        return f"***-{self.__secret_prop_code[-4:]}" # Masks the code for security

    # =================================================================
    # OOP PROPERTY 3: POLYMORPHISM & METHOD OVERRIDING
    # =================================================================
    def perform_act(self):
        """
        Polymorphism in action: Overrides the abstract 'perform_act' method 
        from the parent class to execute Epaja's unique talent performance.
        """
        print(f"\n✨ [Epaja - Polymorphic Act Execution] ✨")
        print(f"Artist: {self.artist_name}")
        print(f"Talent Showcase: {self.primary_talent}")
        print(f"Current Energy: {self.energy_level}%")
        print(f"Secure Prop Access: {self.secret_prop_code}")
        
        if self.energy_level > 50:
            print(f"Action: Epaja dazzles the audience with high-octane execution of '{self.primary_talent}'!")
        else:
            print(f"Action: Epaja delivers a steady, technical performance of '{self.primary_talent}' to conserve energy.")


# =====================================================================
# EXECUTION SCRIPT FOR EPAJA
# =====================================================================
if __name__ == "__main__":
    print("=" * 65)
    print(" INITIALIZING EPAJA'S ADVANCED OOP TALENT MODULE ")
    print("=" * 65)

    # 1. Instantiate Epaja's class
    epaja = EpajaTalentAct(
        artist_name="Epaja",
        stage_category="Multi-Disciplinary Stage Arts",
        primary_talent="Acoustic-Electronic Fusion Guitar & Live Looping",
        initial_energy=90
    )

    # 2. Demonstrating Inheritance (using parent class method)
    print("\n--- Testing OOP Property 1: Inheritance ---")
    epaja.display_artist_info()

    # 3. Demonstrating Encapsulation (Accessing and updating via properties)
    print("\n--- Testing OOP Property 2: Encapsulation ---")
    print(f"Initial Private Energy accessed via getter: {epaja.energy_level}%")
    print(f"Masked Secure Code accessed via getter: {epaja.secret_prop_code}")
    
    # Attempting to assign an invalid energy level to test setter validation
    print("\nAttempting invalid energy assignment (150):")
    epaja.energy_level = 150  

    # Assigning a valid energy level
    print("\nAttempting valid energy assignment (45):")
    epaja.energy_level = 45   

    # 4. Demonstrating Polymorphism (Running the overridden method)
    print("\n--- Testing OOP Property 3: Polymorphism ---")
    epaja.perform_act()
    
    print("\n" + "=" * 65)
    print(" EPAJA'S OOP DEMONSTRATION COMPLETED SUCCESSFULLY ")
    print("=" * 65)
    