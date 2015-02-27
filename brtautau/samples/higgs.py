from .sample import Sample
from .. import NTUPLE_PATH
from .. import log; log = log[__name__]


MASSES = range(60, 205, 5)


class Higgs(Sample):
    pass



class HiggsArray(Higgs):
    """
    """
    def __init__(
        self, cuts=None, 
        ntuple_path=NTUPLE_PATH, **kwargs):

        super(HiggsArray, self).__init__(cuts=cuts, ntuple_path=ntuple_path, **kwargs)
        
        self._sub_samples = []
        self._scales = []
        for mass in MASSES:
            self._scales.append(1)
            self._sub_samples.append(Higgs(
                    ntuple_path=ntuple_path, student='flat_VBF_%s_test' % mass,
                    name='Higgs%s' % mass, label='Higgs%s' % mass))
            
    @property
    def components(self):
        return self._sub_samples

    @property
    def scales(self):
        return self._scales


    def set_scales(self, scales):
        """
        """
        if isinstance(scales, (float, int)):
            for i in xrange(self._sub_samples):
                self._scales.append(scales)
        else:
            if len(scales) != len(self._sub_samples):
                log.error('Passed list should be of size {0}'.format(len(self._sub_samples)))
                raise RuntimeError('Wrong lenght !')
            else:
                for scale in scales:
                    self._scales.append(scale)
        
        log.info('Set samples scales: {0}'.format(self._scales))

 
    def draw_helper(self, *args, **kwargs):
        hist_array = []

        for s in self._sub_samples:
            h = s.draw_helper(*args)
            hist_array.append(h)

        if len(self._scales) != len(hist_array):
            log.error('The scales are not set properly')
            raise RuntimeError('scales need to be set before calling draw_helper')

        hsum = hist_array[0].Clone()
        hsum.reset()
        hsum.title = self.label

        for h, scale in zip(hist_array, self._scales):
            hsum += scale * h

        return hsum
