<h1>Pyramidal tract neurons and Parkinson’s disease in simulated mouse primary motor cortex</h1>
<p>Pyramidal tract neurons are the most direct output to muscles from the primary motor cortex (M1). <a href="https://www.jneurosci.org/content/41/25/5553">Liqiang Chu et al (2021)</a> have shown that layer 5 pyramidal tract neurons (PT5B) decrease in excitability in parkinsonian as compared with control M1 in mice treated with 6-OHDA.
We built this simulation, based on a <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/development/examples/M1detailed">detailed motor cortex implementation in NetPyNE</a>, to see how the changed PT5B neuron excitability changes M1 spiking dynamics.</p>
<p><a href="http://doc.netpyne.org/">NetPyNE</a> is a Python package for creating biological neural networks using the <a href="https://nrn.readthedocs.io">NEURON</a> simulator.</p>
<p>The data that support the findings of this study are openly available on the DANDI Archive (RRID:SCR_017571) at https://doi.org/10.48324/dandi.001444/0.250805.2002</p>
<p>View and analyze our data in DANDI Archive through remote streaming, as demonstrated in the Jupyter notebooks Control_Quiet_Wakefulness.ipynb, Parkinsonian_Quiet_Wakefulness.ipynb, Control_Movement.ipynb, Parkinsonian_Movement.ipynb.</p>
<p>Read the paper <a href="https://doi.org/10.1038/s41531-025-01070-4">Donald W. Doherty et al. (2025).</a></p>
<p>Cite the code: <a href="https://zenodo.org/doi/10.5281/zenodo.12399982"><img src="https://zenodo.org/badge/818711475.svg" alt="DOI"></a></p>
<h2>Acknowlegements</h2>
<p>This research was funded by Aligning Science Across Parkinson's [ASAP-020572] through the Michael J. Fox Foundation for Parkinson's Research (MJFF).</p>
<h2>Parameter settings</h2>
<h3>Control rest</h3>
<p>cfg.ihGbar = 0.75
<p>gbar = 0.0055					# nap		# all secs</p>
<p>gpeak = 7.251280172010002e-05	# kBK		# soma only</p>
<p>cfg.gnafbar = 0.00086 			# NaT		# all secs</p>
<p>cfg.ratesLong = {'TPO': [0,5], 'TVL': [0,2.5], 'S1': [0,5], 'S2': [0,5], 'cM1': [0,2.5], 'M2': [0,2.5], 'OC': [0,5]}</p>
<h3>Parkinsonian rest</h3>
<p>cfg.ihGbar = 0.75
<p>gbar = 0.0055					# nap		# all secs</p>
<p>gpeak = 7.251280172010002e-04	# kBK		# soma only</p>
<p>cfg.gnafbar = 0.0172 			# NaT		# all secs</p>
<p>cfg.ratesLong = {'TPO': [0,5], 'TVL': [0,2.5], 'S1': [0,5], 'S2': [0,5], 'cM1': [0,2.5], 'M2': [0,2.5], 'OC': [0,5]}</p>
<h3>Control activated (movement)</h3>
<p>cfg.ihGbar = 0.25
<p>gbar = 0.0055					# nap		# all secs</p>
<p>gpeak = 7.251280172010002e-05	# kBK		# soma only</p>
<p>cfg.gnafbar = 0.00086 			# NaT		# all secs</p>
<p>cfg.ratesLong = {'TPO': [0,10], 'TVL': [0,10], 'S1': [0,5], 'S2': [0,5], 'cM1': [0,2.5], 'M2': [0,2.5], 'OC': [0,5]}</p>
<h3>Parkinsonian activated (movement)</h3>
<p>cfg.ihGbar = 0.25
<p>gbar = 0.0055					# nap		# all secs</p>
<p>gpeak = 7.251280172010002e-04	# kBK		# soma only</p>
<p>cfg.gnafbar = 0.0172 			# NaT		# all secs</p>
<p>cfg.ratesLong = {'TPO': [0,10], 'TVL': [0,10], 'S1': [0,5], 'S2': [0,5], 'cM1': [0,2.5], 'M2': [0,2.5], 'OC': [0,5]}</p>
