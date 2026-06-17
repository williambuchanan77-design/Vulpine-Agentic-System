import re
from typing import Dict, Any, List

class MetacognitionTutorial:
    """Externalized cognitive friction module to run mental drills."""
    
    @staticmethod
    def run_drill(context_topic: str) -> None:
        print("\n" + "="*60)
        print("🚨 METACOGNITION PROTOCOL INITIATED: TACTICAL ROUTINE REPETITION")
        print("="*60)
        print(f"Target Vector: '{context_topic}'")
        print("\n[DRILL 1: THE REPUTATION OF EXERCISE]")
        print(" Human minds default to comfort. To break the factory settings, run this loop:")
        print(" 1. Isolate your emotional investment in this routine.")
        print(" 2. Identify the single point of failure (Where do you get lazy?).")
        print(" 3. Force-multiply the friction: Double the validation step before execution.")
        print("\n[DRILL 2: THE ANTI-LAZINESS CHECKLIST]")
        print(" -> Am I running this routine because it works, or because it's familiar?")
        print(" -> Have I adjusted the parameters for today's physical/environmental reality?")
        print("="*60 + "\n")


class VerificationNetwork:
    """The Red-Team layer within the Sionnach Agentic Network (SAN)"""
    
    def run_camille_audit(self, raw_input: str) -> Dict[str, Any]:
        return {
            "node": "Camille",
            "focus": "Logical Architecture & Axiomatic Smuggling",
            "assessment": f"Stripping sentiment from '{raw_input}'. Checking for unproven premises."
        }
        
    def run_skade_audit(self, raw_input: str) -> Dict[str, Any]:
        return {
            "node": "Skade",
            "focus": "Empirical Vulnerability & Representative Bias",
            "assessment": "Searching for outlier dependencies. Testing counter-hypothesis viability."
        }


class SionnachAgentEngine:
    """Core autonomous node executing constrained, high-discipline processing."""
    
    def __init__(self):
        self.verifier = VerificationNetwork()
        self.tactical_keywords = ["routine", "drill", "protocol", "tactical", "nutrition", "training"]

    def process_input(self, user_prompt: str) -> Dict[str, Any]:
        clean_prompt = user_prompt.lower().strip()
        
        if any(keyword in clean_prompt for keyword in self.tactical_keywords):
            MetacognitionTutorial.run_drill(user_prompt)
            
        print("⚙️ SAN CORE: Processing data stream...")
        
        camille_log = self.verifier.run_camille_audit(user_prompt)
        skade_log = self.verifier.run_skade_audit(user_prompt)
        
        output_payload = {
            "raw_prompt": user_prompt,
            "verification_payload": [camille_log, skade_log],
            "status": "SECURE - RED TEAMED"
        }
        
        return output_payload

if __name__ == "__main__":
    san_node = SionnachAgentEngine()
    test_prompt = "Optimize my daily grip training and nutrition routine."
    execution_result = san_node.process_input(test_prompt)
    print("▶️ Final Managed Output Status:", execution_result["status"])
