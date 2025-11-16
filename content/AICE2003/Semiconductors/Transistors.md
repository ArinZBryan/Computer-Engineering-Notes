A transistor is a three terminal device that can act as a resistor between two of its terminals, with the resistance of that resistor dependant on the third terminal in some way. Unlike [diodes](./P-N%20Junctions#Diodes%20for%20Digital%20Logic), transistors are able to perform inversion and amplification of a signal, which makes them crucial to almost all of modern electronics. There are three main types of transistor used today: _bipolar junction transistors_ (BJTs), _junction field-effect transistors (JFETs)_ and _metal oxide field-effect transistors_ (MOSFETs). This module only touches upon BJTs and MOSFETs as they are the most commonly used types of transistors.
### Bipolar Junction Transistors
A bipolar junction transistor is made by taking a [P-N junction](./P-N%20Junctions) and simply sticking another semiconductor region onto the end. That is, in a BJT, the semiconductor material may be in one of two configurations: NPN (a small region of P-type semiconductor surrounded by N-type semiconductor) or PNP (a small region of N-type semiconductor surrounded by P-type semiconductor). In an NPN BJT, the majority carrier of current is electrons, but in a PNP BJT, the majority carrier of current is holes.

Because of the structure of a bipolar junction transistor, they may in principle be thought of as two diodes with opposite polarity joined by either their anodes or cathodes depending on which type of transistor is being used. However, that is not quite correct - because the central semiconductor is shared between the junctions, there is an additional 'transistor effect' that occurs which allows for more complex functionality.

| NPN                                 | PNP                                      |
| ----------------------------------- | ---------------------------------------- |
| ![](../images/BJTs/NPN%20Transistor.png) | ![](../images/BJTs/PNP%20Transistor.png) |
The three terminals of a BJT are labelled as the _emitter_, _base_ and _collector_. This is because the _emitter_ emits the majority carrier within the transistor and the _collector_ collects it. The _base_ is not named the way it is for any particular reason. This nomenclature does not change between NPN and PNP transistors.

For the rest of this section, NPN transistors will be considered. However, all the same theory applies to PNP transistors, just in reverse. Electrons and holes flow in opposite directions and where one part of the transistor is in forward bias in an NPN transistor, it will be in reverse bias in a PNP transistor.

All BJTs have four regimes in which they can operate:
- Cut-Off
- Forward Active (Active)
- Saturation
- Reverse Active
In practice, nobody ever uses the reverse active state because it is using the BJT in the complete opposite direction it was designed for. For this reason, it is simply ineffective.

![float-right|200](../images/BJTs/BJT%20Water.png)If the common analogy with electricity and water is used, a BJT could be thought of like a hydraulically actuated valve in a pipe: a continuous pressure (current) needs to be applied to the valve to keep it open to water flow through the main pipe. This is one of the reasons that BJTs are not used in computation, as they constantly require power to operate, rather than just when their state is being switched. This inefficiency makes them simply untenable for use except for where they specifically excel.
##### Cut-Off Regime
A bipolar junction transistor is in the 'cut-off' regime when the voltage between the base and the emitter is less than the [junction barrier voltage](./P-N%20Junctions#Barrier%20Voltage) and both P-N junctions are in [reverse bias](./P-N%20Junctions#P-N%20Junctions%20Under%20Reverse%20Bias). In silicon-based transistors, this is 0.6-0.7V.

![](../images/BJTs/NPN%20BJT%20Cut-Off%20Regime.png)

In this regime, because both junctions are in reverse bias, no majority carriers diffuse between the emitter and carrier and the transistor can be considered 'off'. There is of course a negligible leakage current from what little carrier drift there is across the junctions
##### Active Regime
A bipolar junction transistor is in the 'active' regime when the base/emitter junction is in forward bias, but the base/collector junction is in negative bias. 

Assuming that a transistor is simply just two diodes, you would assume that in this case, there would also be no current flow between the emitter and the collector. However, this is where the transistor effect comes into play. By manufacturing the transistor to ensure that the base is very small, we can make it so that the depletion region between the base and the collector spans much of the base. When electrons move into the base from the collector, some recombine with holes in the base, but overall, not many. Most are instead swept across the depletion region into the collector. This is because the reverse bias of the base/collector junction is only a blocker to the majority carrier - for minority carriers, a reverse bias accelerates them across the barrier.

![](../images/BJTs/NPN%20BJT%20Active%20Regime.png)

It is this acceleration that allows for transistors to act as amplifiers. By varying the current into the base, we can vary the width of the depletion region and thus the amount the electrons are accelerated by. Thus, we have a variable resistor between the emitter and collector, controlled by a small current into the base.

It is for this reason that BJTs are called _bipolar_ - they make use of both holes and electrons to carry current - electrons in the collector and emitter and holes in the base.
##### Saturated Regime
A bipolar junction transistor is in its saturated regime when both P-N junctions are in forward bias. This allows for electrons to flow from both the emitter to the collector and the collector to the emitter. However, we manufacture BJTs to make it so that in the saturated regime they still only _really_ pass current in one direction. To do this, we heavily dope the emitter and lightly dope the base and collector. This means that the flow of electrons in the forward direction (emitter to collector) is significantly larger than the flow of electrons in the reverse direction.

![](../images/BJTs/NPN%20BJT%20Saturated%20Regime.png)
##### Gain
![float-right|300](../images/BJTs/NPN%20BJT%20Currents.png)In a BJT there are three main currents to pay attention to: the current through the emitter, the current through the collector and the current through the base. The emitter current is formed by carriers emitted from the emitter region, the collector current is formed by carriers emitted from the emitter region that make it across the base to the collector and the base current is formed by electron-hole recombination and hole injection.

In the active regime, you get that $I_B << I_E, I_C$ and that as a result, $I_E\approx I_C$. In fact, we actually say there is a coefficient $\alpha$, such that $I_C = \alpha I_E$. We call $\alpha$ the *common base gain*. It can vary from zero to one. We also have the coefficient $\beta$, such that $I_C = \beta I_B$. This is the _common emitter gain_ (also known as current gain) and is the amount by which a change in current at the base will be multiplied by in the change in the current at the emitter. 

$$\alpha=\frac{\beta}{1+\beta}=\frac{I_C}{I_E}\hspace{24pt}\beta=\frac{\alpha}{1+\alpha}=\frac{I_C}{I_B}$$
##### Configurations
In a circuit, a transistor can be connected in three ways: common-base, common-emitter or common-collector. Each of these are used in differing situations, as they provide different output characteristics for given inputs.

![](../images/BJTs/NPN%20BJT%20Configurations.png)

![float-left|200](../images/BJTs/NPN%20BJT%20IV%20graph.png)In general however, the most commonly used configuration is _common-emitter_. In this method of operation, the transistor works as an amplifier with a high 'impedance'. That is, a small voltage change across the base and emitter is amplified as a large change across the collector and emitter.

Depending on the current supplied to the base, you can get differing I/V curves between the collector and emitter and thus, differing levels of amplification.
### Metal-Oxide Field-Effect Transistors
Unlike BJTs, which are _current-controlled_, MOSFETs are _voltage-controlled devices_. It is for this reason that they are used in digital logic for computation rather than BJTs. Because BJTs need current flow just to remain open, they use a lot of power at all times. On the other hand, because MOSFETs only require voltage to remain in a given state, the only current draw is found when switching states. This allows MOSFETs to be significantly more energy efficient when used for computing. On the other hand, MOSFETs are unable to be used as amplifiers, so while useful for switching, they are not a straight upgrade from BJTs.
##### Circuit Symbols
Unlike BJTs, which have only a single circuit symbol for each type (NPN/PNP), MOSFETs have many differing circuit symbols, depending on how they are used and manufactured. 

<table><tbody>
  <tr>
    <td><nobr><strong>P-Type</strong></nobr></td>
    <td><img src="./../images/MOSFETs/IGFET_P-Ch_Enh_Labelled.svg" style="filter:invert(100%);width:5em;height:5em"><img src="./../images/MOSFETs/IGFET_P-Ch_Enh_Diode_Labelled.svg" style="filter:invert(100%);width:5em;height:5em"></td>
    <td><img src="./../images/MOSFETs/IGFET_P-Ch_Enh_Bulk_Labelled.svg" style="filter:invert(100%);width:5em;height:5em"></td>
    <td><img src="./../images/MOSFETs/IGFET_P-Ch_Enh_Labelled_simplified.svg" style="filter:invert(100%);width:12em;height:5em"></</td>
    <td><img src="./../images/MOSFETs/Mosfet_N-Ch_Sedra.svg" style="filter:invert(100%);width:12em;height:5em"></</td>
    <td><img src="./../images/MOSFETs/IGFET_P-Ch_Dep_Labelled.svg" style="filter:invert(100%);width:5em;height:5em"></td>
  </tr>
  <tr>
    <td><nobr><strong>N-Type</strong></nobr></td>
    <td><img src="./../images/MOSFETs/IGFET_N-Ch_Enh_Labelled.svg" style="filter:invert(100%);width:5em;height:5em"><img src="./../images/MOSFETs/IGFET_N-Ch_Enh_Diode_Labelled.svg" style="filter:invert(100%);width:5em;height:5em"></td>
    <td><img src="./../images/MOSFETs/IGFET_N-Ch_Enh_Bulk_Labelled.svg" style="filter:invert(100%);width:5em;height:5em"></</td>
    <td><img src="./../images/MOSFETs/IGFET_N-Ch_Enh_Labelled_simplified.svg" style="filter:invert(100%);width:12em;height:5em"></</td>
    <td><img src="./../images/MOSFETs/Mosfet_N-Ch_Sedra.svg" style="filter:invert(100%);width:12em;height:5em"></</td>
    <td><img src="./../images/MOSFETs/IGFET_N-Ch_Dep_Labelled.svg" style="filter:invert(100%);width:5em;height:5em"></</td>
  </tr>
  <tr>
    <td rowspan="2"></td>
    <td><strong>Body explicitly tied to source</strong></td>
    <td><strong>Exposed body terminal</strong></td>
    <td colspan="2"><strong>Body terminal not shown</strong></td>
    <td><strong>Body explicitly tied to source</strong></td>
  </tr>
  <tr>
    <td colspan="4"><strong>Enhancement Mode</strong></td>
    <td><strong>Depletion Mode</strong></td>
  </tr>
</tbody>
</table>
